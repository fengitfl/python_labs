def format_record(s):
    for i in s:
        if len(s) != 3:
            if not i:
                return "ValueError"

    fio=s[0]
    fio=fio.split()
    if type(s[2]) != float:
        return "TypeError"
    if 1<s[2]>5:
        return "ValueError"

    try:fio_ready=('"'+fio[0].capitalize()+ " " + fio[1][0].upper()+"."+fio[2][0].upper()+".")
    except IndexError : fio_ready=('"'+fio[0].capitalize()+ " " + fio[1][0].upper()+".")


    group=f"гр. {s[1]}"

    gpa=f"{s[2]:.2f}"
    gpa_ready=(gpa+'"')
    end = f"{fio_ready}, {group}, {gpa_ready}"
    return end





