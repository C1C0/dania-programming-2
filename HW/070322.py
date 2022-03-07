class Solutions:
    
    def __init__(self) -> None:
        self.listToPopulate = []

    def firstTask(self) -> bool:
        a = None
        
        print("Write: 'ok' if wanna get out of loop\n\n")

        # Get list
        while str(a).lower() != 'ok':
            try:
                a = input("Insert a number: ")
                self.listToPopulate.append(int(a))  
            except:
                print("Provided variable '" + a + "' is not a number.")
                
        if len(self.listToPopulate) != 8:
            return False
                
        # Check list
        if self.listToPopulate.count(self.listToPopulate[4]) == 3:
            return True

        return False

    def secondTask(self) -> float or int:
        output = 1
        
        for i in self.listToPopulate:
            output *= i
            
        return output
    
    def fourthTask(self, listOfDisctionaries) -> dict:
        output = {}
        
        for dict in listOfDisctionaries:
            output |= dict
            
        return output
    
    def sixthTask(self, string: str) -> dict:
        output = {}
        
        for ch in string:
            if ch in output.keys():
                output[ch] += 1
            else:
                output[ch] = 1
                
        return output
            

solutions = Solutions()

"""
1. Write a Python program that accept a list of integers and check 
the length and the fifth element. Return true if the length of the 
list is 8 and fifth element occurs thrice in the said list.

Input:
[19, 19, 15, 5, 5, 5, 1, 2]
Output:
True
Input:
[19, 15, 5, 7, 5, 5, 2]
Output:
False
Input:
[11, 12, 14, 13, 14, 13, 15, 14]
Output:
True
Input:
[19, 15, 11, 7, 5, 6, 2]
Output:
False

"""

print(solutions.firstTask())


"""
2. Write a python function to multiply all the numbers in a list

Sample List : (8, 2, 3, -1, 7)
Expected Output : -336
"""

print(solutions.secondTask())

"""
3. Write a python program to reverse a string

Sample String : "1234abcd"
Expected Output : "dcba4321"
"""

print(input("Write Me anything and I reverse it !\n")[::-1])

"""
4. Write a Python script to concatenate following dictionaries to create a new one

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""

print(solutions.fourthTask([{1:10, 2:20}, {3:30, 4:40}, {5:50, 6:60}]))

"""
5. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.

Expected Output : 0 1 2 4 5
"""

for i in range(7):
    if i == 6 or i == 3:
        continue
    
    print(i, end=' ')

"""
6. Write a Python program to count the number of characters (character frequency) in a string

Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
"""

print(solutions.sixthTask(input("\n\nWrite a string: ")))