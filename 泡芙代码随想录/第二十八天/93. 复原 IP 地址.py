class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        self.back_tracking(s, 0, [], result)
        return result

    def back_tracking(self, s, start_index, path, result):
        if len(path) == 4 and start_index == len(s):
            result.append('.'.join(path))
            return
        if len(path) == 4:
            return
        for l in range(1, 4):
            if start_index + l - 1 < len(s):
                if l > 1 and s[start_index] == '0':
                    return
                part = s[start_index: start_index + l]
                if int(part) <= 255:
                    path.append(part)
                    self.back_tracking(s, start_index + l, path, result)
                    path.pop()
                else:
                    return
