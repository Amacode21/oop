
def show_datas(container:list, data:str) -> None:
    if len(container) < 1:
        print('No records found')
        return
    for _ in container[data]:
        for v in _.values():
            """
                This will print the class string representation of each student.
            """
            print(f'{v}')
        print('------')