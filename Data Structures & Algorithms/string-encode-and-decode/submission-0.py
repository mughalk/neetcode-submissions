class Solution:

    def encode(self, strs: List[str]) -> str:
        send_this_str=""
        # need some sort of delimiter, but that delimiter is a symbol and should not be
        # used as a "true delimiter". it should only act as a symbol and we must count the length to
        # be truly sure of our message's contents

        #ie ["hello","world"]
        if not strs:
            return ""
        final_str=""
        for s in strs:
            send_this_str+=str(len(s))
            send_this_str+=','
            final_str+=s
        send_this_str+="#"
        send_this_str+=final_str
        # need to send a sizelist separated by a comma and a #
        return send_this_str

    def decode(self, s: str) -> List[str]:
        #ie "50,5#helloworld"
        str_lst = []
        word = ""
        iter_len = len(s)
        i=0
        j=0
        size_lst=[]
        parts=s.split("#",1)
        if len(parts)==1:
            #empty, nothing to decode
            return []
        size_lst=parts[0]
        words=parts[1]
        if not size_lst:
            return[]
        
        length_vals=[]
        for x in size_lst.split(','):
            if x:
                length_vals.append(int(x))
        iter_len=len(length_vals)
        pos=0
        for L in length_vals:
            str_lst.append(words[pos:pos+L])
            pos+=L
        return str_lst
        # for c in s:
        #     char_len = int(c)
            # have to have 2 pointers?


