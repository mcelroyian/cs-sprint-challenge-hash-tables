# Your code here
import os


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    d = {}
    result = []
    for path in files:
        file = os.path.basename(path)
        if file not in d.keys():
            d[file] = []
        d[file].append(path)
    for q in queries:
        if q in d.keys():
            for path in d[q]:
                result.append(path)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
