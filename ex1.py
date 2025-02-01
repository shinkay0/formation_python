def get_max_note(tab1, tab2):
  best_note1 = max(tab1)
  best_note2 = max(tab2)
  
  if best_note1 > best_note2:
    return best_note1
  else:
    return best_note2
  

student1 = input("Entrer le nom du premier élève : ")
student2 = input("Entrer le nom du premier élève : ")

student1_notes = [0] * 3
student2_notes = [0] * 3

i = 0

print(f"Notes de {student1}")
for i in range(3):
  note = -1
  while note < 0 or note > 20:
    note = int(input("Entrer une note : "))
    student1_notes[i] = note


print(f"Notes de {student2}")
for i in range(3):
  note = -1
  while note < 0 or note > 20:
    note = int(input("Entrer une note : "))
    student2_notes[i] = note


print(student1_notes)
print(student2_notes)

print(get_max_note(student1_notes, student2_notes))


