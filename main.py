from pyscript import document


#base variables for the members
BatchA = {"Jimmy Blanka","Cammy White"}
BatchB = {"Ken Masters", "Chun Li", "Charlie Nash"}
BatchC = {"Mason Bison", "William Guile"}
BatchD = {"Victor Sagat", "Charlie Nash"}


combine_set = BatchA | BatchB | BatchC | BatchD  

def add_fighter(e):
    global combine_set

    Fname = document.getElementById("first_name").value
    Lname = document.getElementById("last_name").value

    full_name = Fname + " " + Lname
    new_set = {full_name}

    combine_set = combine_set | new_set

    names_sort = sorted(list(combine_set))

    list_str = "<br> - ".join(names_sort)
    size = len(combine_set)

    target_zone = document.getElementById("output")
    target_zone.innerHTML = f"All members are:<br> - {list_str}<br><br>Total fighter count: {size}"

    document.getElementById("first_name").value = " "
    document.getElementById("last_name").value = " "
