# Lecture notes from Computational Python 2019

## Monday 14.10.2019

- If we have a list with non-unique elements, by using set() we can get the list of unique elements.

- Indendation is key for dividing up code between i.e. normal code and part of a for loop.

- In range(1,4) last value is not included.

- Variable definitions inside a function cannot be seen from outside i.e. variables within a function have their function as their scope.

- In python3 the order of the dictionary entries are preserved from when they where created.

## Tuesday 15.10.2019

- Testing is tedious but worth it in the long run. It also enforces progamming in smaller chunks!

- `-m` flag searches for the module given directly afterwards.

- Make pyhton environmnets with `python3 -m venv myenv` for installing specialised packages without affecting the main installation. 
    - Activate these new environmnets with `source myenv/bin/activate`.

- pytest is superior to nosetest for python code testing.

- These two operators are useful and complementary:
    - `%` computes remainder after division.
    - `//` computes integer divison. 

- "Refactoring" in coding implies shortening and making a code more legible or prettier without modifying the implementation. It is a usual second step after first implementation.

- pytest fixtures can help with testing.

- f strings (`f"{string}"`) converts expressions with more complex variables into a string. Introduced in python3.6. Makes string outputs easier to read.

- Phylosophy: write tests before code! (www.pythontesting.net).

- **Assignmnets**: usual pitfall, beware:
    - We create an array `x=numpy.zeros(2)` -> `x = [0 0]`.
    - We create `y=x` -> `y = [0 0]`, **nothing new is created!** We are only giving the object `[0 0]` a new name! `y = x = [0 0]`.
    - If we now modify x, y will also be modified: `x = [1 0]` then `y = [0 0]`.
    - To avoid this do, `y=x.copy()`.
    - To check if two objects are the same of different use `x is y`.
 
 - Numpy is memory conservative, i.e. if in doubt probably the generation of an new variable from an old one is most probably **not** making a copy.

 - Numpy array operations are comparable to the speed of C/Fortran.

 - By exectuing a script on interactive mode `python3 -i myscript.py` runs the script and drops you in an interative python shell just after the execution with all variables loaded (same as matlab execution).

 - Shortcut to matrix multiplication: "munpy.dot(a,b) == a @ b".

 - Matrix class exists but is not really used in practice.

 - A subclass inherits definitions that are not specified for its class but were for its parent class.

 ## Wednesday 16.10.2019

 - To modify an input for file creation:
    - Generate the input string with `in_file="""input {value}"""`.
    - Then the magnitude of `{value}` can be changed on creation with something like `with open('file.dat','w') as f:` followed by `f.write(in_file.format(value=0.1))`. This generates file.dat substituting the `{value}` by the magnitude 0.1.

- Use `subprocess.run(['command1','command2'])` to run different commands in the shell through python.

- Pandas (np for short) is relevant for database generation and manipulation. Main variables types are np.series (1D) and np.DataFrame (2D).

 ## Thursday 17.10.2019

 - pdb and pydb two different python debuggers but the standard pdb is "good enough".

 - Review the topic of iterators as they can be relevant.