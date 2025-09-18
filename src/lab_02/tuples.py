def format_record(s):
    for i in s:
        if i!=3:
            if not i:
                return "ValueError"
    fio=s[0]
    fio=fio.split()
    try:fio_ready=('"'+fio[0].capitalize()+ " " + fio[1][0].upper()+"."+fio[2][0].upper()+".")
    except IndexError : fio_ready=('"'+fio[0].capitalize()+ " " + fio[1][0].upper()+".")

    group=f"гр. {s[1]}"

    gpa=f"{s[2]:.2f}"
    gpa_ready=(gpa+'"')
    end = f"{fio_ready}, {group}, {gpa_ready}"
    return end



print(format_record(s=["Иванов Иван Иванович", "BIVT-25", 4.6]))
print(format_record(s=["Петров Пётр", "IKBO-12", 5.0]))
print(format_record(s=["Петров Пётр Петрович", "IKBO-12", 5.0]))
print(format_record(s=["  сидорова  анна   сергеевна ", "ABB-01", 3.999]))
print(format_record(s=["","BIVT-25",3.999]))


