"""Walkthrough test for calculate_prf."""

import importlib

import pandas as pd
import pytest
from rdflib import Graph

evaluate = importlib.import_module("blinkg.evaluate")


def test_calculate_prf_walkthrough(monkeypatch):
    # Similarity mocked to exact string equality.
    exact = lambda pred_value, gt_value, *args: 1.0 if pred_value == gt_value else 0.0
    for name in ("calculate_levenshtein", "calculate_bert", "calculate_bert_lex"):
        monkeypatch.setattr(evaluate, name, exact)

    gt = pd.DataFrame([
        {"Entity Class": "gtfs:Stop",  "Datatype": "xsd:string", "Join": ""},   # g0
        {"Entity Class": "gtfs:Route", "Datatype": "",           "Join": ""},   # g1
        {"Entity Class": "gtfs:Trip",  "Datatype": "xsd:int",    "Join": ""},   # g2
    ])
    pred = pd.DataFrame([
        {"Entity Class": "gtfs:Stop",   "Datatype": "",           "Join": ""},  # p0
        {"Entity Class": "gtfs:Agency", "Datatype": "xsd:string", "Join": ""},  # p1
        {"Entity Class": "gtfs:Shape",  "Datatype": "",           "Join": ""},  # p2
    ])
    # p0-g0 and p1-g1 matched. p2 invented, g2 never produced.
    assigned_pairs = [(0, 0), (1, 1)]

    result = evaluate.calculate_prf(
        pred, gt, assigned_pairs,
        common_cols=["Entity Class", "Datatype", "Join"],
        ontology=Graph(),
    )

    # Entity Class: one right, one wrong, one invented, one missed.
    assert result["Entity Class"] == {
        "TP": 1, "FP": 2, "FN": 2,
        "precision": pytest.approx(1 / 3),
        "recall": pytest.approx(1 / 3),
        "f1": pytest.approx(1 / 3),
    }

    # Datatype: one left blank where required, one filled where it must stay empty, one missed.
    assert result["Datatype"] == {
        "TP": 0, "FP": 1, "FN": 2,
        "precision": 0.0, "recall": 0.0, "f1": 0.0,
    }

    # Join: empty on both sides everywhere, nothing to grade.
    assert result["Join"] == {
        "TP": 0, "FP": 0, "FN": 0,
        "precision": None, "recall": None, "f1": None,
    }

    # Every non-empty GT cell is TP or FN, every non-empty pred cell is TP or FP.
    for col in result:
        assert result[col]["TP"] + result[col]["FN"] == int((gt[col] != "").sum())
        assert result[col]["TP"] + result[col]["FP"] == int((pred[col] != "").sum())
