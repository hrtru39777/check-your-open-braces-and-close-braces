def check(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        return "not found a file"
    except Exception as e:
        return f"error: {e}"

    # count of {
    open_braces = 0
    # count of }
    close_braces = 0
    # now line count 
    line= 0
    for line in lines:
        # step next line 
        line_number += 1

        # count { and }
        for char in line:
            if char == '{':
                open_braces += 1
            elif char == '}':
                close_braces += 1
    # The difference between { and }
    brace_diff = open_braces - close_braces

    if brace_diff == 0:
        return f"open braces and close braces are coorect."
    else:
        return f"difference of open braces and close braces: {brace_diff} (open braces: {open_braces}, close braces: {close_braces})"




# set your file path which you want to check
file_path = '.'
result = check_braces_in_rtf(file_path)
print(result)
