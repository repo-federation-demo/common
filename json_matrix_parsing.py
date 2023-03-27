import sys

# Purpose of this script is to take in a map/dict that enumerate the matrix space, and output
# the list of key/value pairs in a way that we can pass to something that accepts such a list.
# For example, the "with" clause for a docker build job has build_args that will accept this
# content.
if __name__ == "__main__":
    import json
    parsed_build_args = json.loads(sys.argv[1])
    parsed_matrix = json.loads(sys.argv[2])
    #
    for k in parsed_build_args.keys():
        print(f"{k}={parsed_matrix[k]}")
