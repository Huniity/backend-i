# Generate Lines for txt file
with open("hello.txt", "w") as f:
    for _ in range(93763):
        f.write("Hello world \n\n")

class ReaderFile():
    def __init__(self):
        pass
        
    def countLines(self):
        count = 0
        with open("hello.txt", "r") as f:
            f.readline()
            for line in f:
                count += 1
            print(f"There is a total of {count} lines in your current {f}")
    
    def countWhiteSpace(self):
        pass

    def countEmptyLines(self):
        count = 0
        with open("hello.txt", "r") as f:
            f.readline()
            for line in f:
                if line == '\n':
                    count += 1
            print(f"There is a total of {count} empty in your current {f}")
        pass


reader = ReaderFile()

reader.countLines()
reader.countEmptyLines()