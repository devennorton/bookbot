
def get_book_text(fp: str) -> int:
    try:
        with open(fp) as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: '{fp}' not found")
    except Exception as e:
        print(f"Unexpected error occured printing contents of '{fp}': {e}")

def get_word_count(bt: str) -> int:
    return len(bt.split())

def get_char_counts(bt: str) -> dict[str, int]:
    cs = {}
    for c in bt.lower():
        cs[c] = cs.get(c, 0) + 1
    return cs

def char_count_report(cr: dict[str,int]) -> str:
    rpt = []
    for ch, count in cr.items():
        rpt.append({"char": ch, "num": count})
    rpt.sort(key=lambda x: x["char"])
    return "\n".join([f"{x['char']}: {x['num']}" for x in rpt])
