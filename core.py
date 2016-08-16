import sys

def reverse_hash(hashval):
    letters = "acdegilmnoprstuw"
    result = []
    
    while hashval != 7:
        try:
            result.append(letters[hashval % 37])
        except IndexError:
            raise ValueError("Invalid hash value supplied")

        hashval = hashval/37

    return ''.join(reversed(result))


if __name__ == "__main__":
    try:
        print reverse_hash(int(sys.argv[1]))
    except IndexError:
        print " Format:\n=========\n\tpython core.py <hash_value>"
    except ValueError:
        print "Invalid hash value supplied"
