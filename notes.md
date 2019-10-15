# Lecture notes from Computational Python 2019

## Monday 14.10.2019

- If we have a list with non-unique elements, by using set() we can get the list of unique elements.

- Indendation is key for dividing up code between i.e. normal code and part of a for loop

- In range(1,4) last value is not included

- Variable definitions inside a function cannot be seen from outside i.e. variables within a function have their function as their scope

- In python3 the order of the dictionary entries are preserved from when they where created

## Tuesday 15.10.2019

- Testing is tedious but worth it in the long run. It also enforces progamming in smaller chunks!

- "-m" flag searches for the module given directly afterwards

- Make pyhton environmnets with "python3 -m venv myenv" for installing specialised packages without affecting the main installation. 
    - Activate these new environmnets with "source myenv/bin/activate"

- pytest is superior to nosetest for python code testing

- These two operators are useful and complementary:
    - "%" computes remainder after division
    - "//" computes integer divison. 

- "Refactoring" in coding implies shortening and making a code more legible or prettier without modifying the implementation. It is a usual second step after first implementation.

- pytest fixtures can help with testing

- "f strings" converts expressions with more complex variables into a string. Introduced in python3.6. Makes string outputs easier to read.

- Phylosophy: write tests before code!