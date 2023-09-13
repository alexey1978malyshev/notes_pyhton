MAIN_DIR = abspath(dirname(__file__))

def input_note() -> list:
    note_input = []
    note_input.append(input("Введите название заметки: "))
    note_input.append(input("Введите текст заметки: "))

    return note_input


def create(notes_loc: dict, note: list, idc: int) -> tuple[dict, int]:
    idc += 1
    notes_loc[idc] = note
    return notes_loc, idc


def export_note_dict_to_csv(notes_loc: dict, file_name: str):
    full_name = join(MAIN_DIR, file_name + '.csv')
    df = pd.DataFrame(notes_loc)
    df.to_csv(full_name, index=False, header=True)


def read_from_csv(file_name):
    full_name = join(MAIN_DIR, file_name + '.csv')
    df = pd.read_csv(full_name, index_col=False)
    print(df)


def search_note_by_name(notes_loc: dict, searchstr: str) -> int:
    for key, val in notes_loc.items():
        if val[0].startswith(searchstr):
            return key


def delete_note_by_name(notes_loc: dict, delete_note: str):
    for key, val in notes_loc.items():
        if val[0].startswith(delete_note):
            del notes_loc[key]
            break


def update_note(notes_loc: dict, up_note_name: str):
    for key, val in notes_loc.items():
        if val[0].startswith(up_note_name):
            val.clear()
            val.append(input("Введите название заметки: "))
            val.append(input("Введите текст заметки: "))

