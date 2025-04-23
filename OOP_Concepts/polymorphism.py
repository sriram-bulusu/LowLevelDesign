# POLYMORPHISM

"""
    Polymorphism is aka method overriding. This means that different objects can use the same method of the parent class
    in different ways.

    For example, a specific chess piece moves in a certain way. But, the parent class (ChessPiece) will have it's own move method

    However, for this to work, each individual class must share a common interface. This common interface can be a class or a
    method.
"""

# COMMON INTERFACE: CLASS
class Document():
    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")
    
class PDF(Document):
    def show(self):
        return "Show PDF format.pdf"

class Word(Document):
    def show(self):
        return "Show Word format.docx"

testDoc = Document()
docs = [PDF(), Word()]

testDoc.show() # will raise an error because the subclass did not implement the show method

for doc in docs:
    print(doc.show())



# COMMON INTERFACE: METHOD
class Bishop():
    def move(self):
        print("Bishops can move diagonally")

class King():
    def move(self):
        print("Kings can move only one square in any direction")

# this method is the interface that both classes are sharing
def testMove(piece):
    piece.move()

bishop = Bishop()
king = King()

testMove(bishop)
testMove(king)