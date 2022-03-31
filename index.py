def top_note(student):

    # return {"name": student["name"], "top_note": max(student["notes"])}

    student["top_note"] = max(student["notes"])
    student.pop("notes")
    return student


    # name_note = [x for x in student.values()][0]
    # max_notes = max([i for i in student.values()][1])
    #
    # key = ["name", "top_note"]
    # value = [name_note, max_notes]
    #
    # student = dict(zip(key, value))
    # return student


    # student.popitem()
    # student.update({"top_note":max_notes})
    # return student

print(top_note({"name": "Jaqueline", "notes":[5, 4, 3]}))
print(top_note({"name": "Eduardo", "notes":[3,3,3]}))
print(top_note({"name": "Mauricio", "notes":[1,2,3]}))
print(top_note({"name": "Nathan", "notes":[1,4,6]}))
