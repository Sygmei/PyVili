# PyVili

PyVili is a Python API to manipulate Vili Data files

You can install it using the following command : `pip install vili`

## What does vili files look likes ?

```yaml
Person: # This is how you define a ComplexNode (object)
    animal:"Homo Sapiens" # You can use strings
    legs:2 # And also integers
    arms:2

Cat:
    animal:"Felis silvestris catus"
    legs:4

Jack(Person):
    criminal:True # You can use booleans (True / False)
    age:32
    name:"Jack"
    surname:"Sparrow"
    weight:76.4 # Vili also support floats

Billy(Cat):
    activities:[ # A simple list
        "Chasing mice",
        "Eating food"
        "Sleeping"
    ]

House:
    inhabitants:
        billy:&Billy # You can reference an existing object
        jack:&Jack
```