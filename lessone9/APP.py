def search_names(names_list, search_term):
    """
    在名字列表中搜尋包含特定字詞的名字。

    Args:
        names_list (list): 包含名字的列表 (字串)。
        search_term (str): 要搜尋的字詞。

    Returns:
        list: 包含搜尋字詞的符合名字列表。
    """
    found_names = []
    if not search_term: # 如果搜尋字詞為空，則不進行搜尋
        return found_names

    for name in names_list:
        if search_term.lower() in name.lower(): # 忽略大小寫進行比對
            found_names.append(name)
    return found_names

if __name__ == "__main__":
    # 預設的名字資料
    names_data = [
        "Alice Wonderland",
        "Bob The Builder",
        "Charlie Brown",
        "David Copperfield",
        "Eve Adamson",
        "Alicia Keys",
        "Charles Xavier"
    ]

    print("目前名字資料庫:")
    for n in names_data:
        print(f"- {n}")
    print("-" * 20)

    while True:
        query = input("請輸入要搜尋的字詞 (或輸入 'exit' 離開): ")
        if query.lower() == 'exit':
            print("感謝使用，再見！")
            break

        if not query.strip(): # 檢查是否只輸入空白
            print("請輸入有效的搜尋字詞。")
            continue

        results = search_names(names_data, query)

        if results:
            print(f"\n找到符合 '{query}' 的名字:")
            for name in results:
                print(f"- {name}")
        else:
            print(f"\n找不到任何包含 '{query}' 的名字。")
        print("-" * 20)
