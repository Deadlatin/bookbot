def word_count(text):
    words = text.split()
    count = len(words)
    return count

def char_count(text):
    text = text.lower()
    a_count = text.count("a")
    b_count = text.count("b")
    c_count = text.count("c")
    d_count = text.count("d")
    e_count = text.count("e")
    f_count = text.count("f")
    g_count = text.count("g")
    h_count = text.count("h")
    i_count = text.count("i")
    j_count = text.count("j")
    k_count = text.count("k")
    l_count = text.count("l")
    m_count = text.count("m")
    n_count = text.count("n")
    o_count = text.count("o")
    p_count = text.count("p")
    q_count = text.count("q")
    r_count = text.count("r")
    s_count = text.count("s")
    t_count = text.count("t")
    u_count = text.count("u")
    v_count = text.count("v")
    w_count = text.count("w")
    x_count = text.count("x")
    y_count = text.count("y")
    z_count = text.count("z")
    letter_count = {
        "a": a_count,
        "b": b_count,
        "c": c_count,
        "d": d_count,
        "e": e_count,
        "f": f_count,
        "g": g_count,
        "h": h_count,
        "i": i_count,
        "j": j_count,
        "k": k_count,
        "l": l_count,
        "m": m_count,
        "n": n_count,
        "o": o_count,
        "p": p_count,
        "q": q_count,
        "r": r_count,
        "s": s_count,
        "t": t_count,
        "u": u_count,
        "v": v_count,
        "w": w_count,
        "x": x_count,
        "y": y_count,
        "z": z_count
    }
    return letter_count

def sort_on(items):
    return items["num"]

def list_sort(dict):
    list = []
    for letter in dict:
        tmp_dict = {}
        tmp_dict["char"] = letter
        tmp_dict["num"] = dict[letter]
        list.append(tmp_dict)
    list.sort(reverse=True,key=sort_on)
    return list