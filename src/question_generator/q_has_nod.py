import random

only_nod_template_with_premise = ["以下の意見に賛成意見が出ています！別の考えの方はいますか？\n　「[<title>]\n<s1>\n<s2>」", \
                                  "ぜひ、このコメントについて返信をしてください！\n　「[<title>]\n<s1>\n<s2>」"]



def has_nod_q_generator(post, si, thread_title):
    select_template = random.choice(only_nod_template_with_premise)

    claim_s = post.sentences[si].body

    if si > 1:
        if post.sentences[si - 1].tag == "PREMISE":
            premise_s = post.sentences[si - 1].body
            return select_template.replace("<title>", thread_title).replace("<s1>", premise_s).replace("<s2>", claim_s)
    elif len(post.sentences) > si + 2:
        if post.sentences[si + 1].tag == "PREMISE":
            premise_s = post.sentences[si + 1].body
            return select_template.replace("<title>", thread_title).replace("<s1>", claim_s).replace("<s2>", premise_s)

    return select_template.replace("<title>", thread_title).replace("<s1>", claim_s).replace("<s2>", "")