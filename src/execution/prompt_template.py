import sys
import argparse

#Select the needed fields
header_list = [ 
    "Data Reference",
    "Ontology Property",
    "Entity Class",
    "Related Entity Class",
    "Subject Generation",
    "Join",
    "Datatype",
    #"Language Annotations",
    "Function Name",
    "Function Output"
]

def main():

    parser = argparse.ArgumentParser(
        description="Generate a prompt template for knowledge graph mapping based on input files, ontology file, and optional SKOS file."
    )

    # Argument for input files: -i, requires 1 or more values.
    parser.add_argument(
        '-i', '--input', 
        nargs='+',
        required=True,
        help='List of input files to process.'
    )
    
    # Argument for the ontology file: -g, requires 1 value.
    parser.add_argument(
        '-g', '--ontology',
        required=True,
        help='Ontology file (e.g., an RDF/OWL file).'
    )
    
    # Argument for the SKOS file: -s, requires 1 value.
    parser.add_argument(
        '-s', '--skos',
        required=False,
        default=None,
        help='SKOS file (Simple Knowledge Organization System).'
    )
    
    # Argument for the output file: -o, requires 1 value.
    parser.add_argument(
        '-o', '--output',
        required=False,
        default='prompt.txt',
        help='Output file where the result will be written.'
    )
    
    try:
        args = parser.parse_args()
    except Exception as e:
        print(f"Error parsing arguments: {e}", file=sys.stderr)
        sys.exit(1)

    
    print(f"Input files (-i): {args.input}")
    print(f"Ontology file (-g): {args.ontology}")
    print(f"SKOS file (-s): {args.skos}")
    print(f"Output file (-o): {args.output}")
    
    try:
        with open(args.output, 'w') as outfile:
            if len(args.input) > 1:
                prompt_template = "I have these input files and I want to build a knowledge graph with all possible mappings between them using this ontology. Could you make a table with the data references and a links to the corresponding ontology properties? Link all the properties that you can with the information that you have. Provide also the class of the entities or both the classes that they relate to, and a way to generate the subject of them. Use the following header:"
            else:
                prompt_template = "I have this input file and I want to build a knowledge graph with all possible mappings between them using this ontology. Could you make a table with the data references and a links to the corresponding ontology properties? Link all the properties that you can with the information that you have. Provide also the class of the entities or both the classes that they relate to, and a way to generate the subject of them. Use the following header:"
            for header in header_list:
                prompt_template += " "+header+","
            prompt_template = prompt_template.rstrip(",")
            prompt_template += "."
            prompt_template += "\n\n"
            
            for input_file in args.input:
                prompt_template += f"{input_file}\n"
                try:
                    with open(input_file, 'r') as infile:
                        content = infile.read()
                        prompt_template += content + "\n"
                except FileNotFoundError as e:
                    print(f"Input file not found: {input_file}: {e}", file=sys.stderr)
                except IOError as e:
                    print(f"I/O Error reading '{input_file}': {e}", file=sys.stderr)

            try:
                with open(args.ontology, 'r') as onfile:
                    content = onfile.read()
                    prompt_template += args.ontology + "\n" + content + "\n"
            except FileNotFoundError as e:
                print(f"Input file not found: {input_file}: {e}", file=sys.stderr)
            except IOError as e:
                print(f"I/O Error reading '{input_file}': {e}", file=sys.stderr)

            if args.skos:
                try:
                    with open(args.skos, 'r') as skosfile:
                        content = skosfile.read()
                        prompt_template += args.skos + "\n" + content
                except FileNotFoundError as e:
                    print(f"SKOS file not found: {args.skos}: {e}", file=sys.stderr)
                except IOError as e:
                    print(f"I/O Error reading SKOS file '{args.skos}': {e}", file=sys.stderr)

            outfile.write(prompt_template)

    except IOError as e:
        print(f"I/O Error handling files: {e}", file=sys.stderr)
        sys.exit(1)
        sys.exit(1)

if __name__ == "__main__":
    main()