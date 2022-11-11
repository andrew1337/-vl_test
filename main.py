import json
import difflib


def build_synonyms_mapping(dictionary: list) -> "list[set]":
    result = []
    for i, j in dictionary:
        i, j = i.lower(), j.lower()
        was_added_to_mapping = False
        for index, synonym_set in enumerate(result.copy()):
            if i in synonym_set or j in synonym_set:
                result[index].add(i)
                result[index].add(j)
                was_added_to_mapping = True
                for index1, psm1 in enumerate(result.copy()):  # merge sets of synonyms
                    for index2, psm2 in enumerate(result.copy()):
                        if index1 == index2:
                            continue
                        if psm1.intersection(psm2):
                            result[index1].update(psm2)  # updates every set
        if not was_added_to_mapping:
            result.append({i, j})
    return result


def is_synonyms(a: str, b: str, list_of_sets) -> bool:
    a, b = a.lower(), b.lower()
    candidates = {a, b}
    if len(candidates) == 1:
        return True
    for synonym_set in list_of_sets:
        if candidates.issubset(synonym_set):
            return True
    return False


def check_synonyms(
    dictionary: "list[list[str]]", queries: "list[list[str]]"
) -> "list[bool]":
    print(dictionary)
    print(queries)
    result = []
    mapping = build_synonyms_mapping(dictionary)
    for i, j in queries:
        result.append(is_synonyms(i, j, mapping))
    print(result)
    raise
    return result


def main(file_name: str, out_file_name: str) -> None:
    with open(file_name) as f_input:
        data = json.load(f_input)
        test_cases = data.get("testCases")
        with open(out_file_name, "w") as f_out:
            for test_case in test_cases:
                query_result = check_synonyms(
                    test_case["dictionary"], test_case["queries"]
                )
                for i in query_result:
                    answer = "synonyms" if i else "different"
                    f_out.write(f"{answer}\n")


def files_are_same(path_1, path_2) -> bool:
    with open(path_1) as file_1:
        file_1_text = file_1.readlines()
    with open(path_2) as file_2:
        file_2_text = file_2.readlines()
    for _ in difflib.unified_diff(
        file_1_text, file_2_text, fromfile=path_1, tofile=path_2, lineterm=""
    ):
        return False
    return True


if __name__ == "__main__":
    main("input/example.in.json", "output/my.out")
    assert files_are_same("test_output/example.out", "output/my.out")
    main("input/example_big.in.json", "output/my_big.out")
    assert files_are_same("test_output/example_big.out", "output/my_big.out")
    main("input/input.json", "output/output.out")


dictionary = [
    ["big", "large"],
    ["large", "huge"],
    ["great", "huge"],
    ["small", "little"],
    ["apple", "banana"],
]
test_case = [
    ["same", "same"],
    ["big", "huge"],
    ["huge", "big"],
    ["apple", "peach"],
    ["big", "tall"],
    ["peach", "PEACH"],
]

expected_result = [True, True, True, False, False, True]
