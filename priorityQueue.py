import math

class QueueElement:
    def __init__(self, element, priority):
        self.element = element
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        leftPointer = 0
        rigthPointer = len(self.queue) - 1

        while leftPointer <= rigthPointer:
            middlePointer = math.floor((rigthPointer + leftPointer) / 2)
            currentPriority = self.queue[middlePointer].priority

            if currentPriority == element.priority:
                self.queue.insert(middlePointer, element)
                return
            elif element.priority > currentPriority:
                if middlePointer + 1 < len(self.queue) and self.queue[middlePointer + 1].priority >= element.priority:
                    self.queue.insert(middlePointer + 1, element)
                    return
                else:
                    leftPointer = middlePointer + 1
            else:
                if middlePointer - 1 > 0 and self.queue[middlePointer - 1].priority <= element.priority:
                    self.queue.insert(middlePointer, element)
                    return
                else:
                    rigthPointer = middlePointer - 1
        
        if leftPointer == 0:
            self.queue.insert(0, element)
        elif rigthPointer == len(self.queue) - 1:
            self.queue.append(element)
    
    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        return None

    def isEmpty(self):
        return (len(self.queue) == 0)