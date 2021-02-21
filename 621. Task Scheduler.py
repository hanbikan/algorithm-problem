#name amount cooldown
class Solution:
    def leastInterval(self, tasks, n):
        RET = []
        priority = self.get_task_priority(tasks)
        while True:
            print(priority)
            amount_amount = 0
            i_ready = None
            for i in range(len(priority)): #DEL/SELECT/COOLDOWN-1
                amount_amount += priority[i][1]
                
                if priority[i][1] == 0: #del
                    del priority[i]
                else:
                    if priority[i][2] == 0: #select
                        if i_ready == None: i_ready = i
                    elif priority[i][2] >= 1: #cooldown-1
                        priority[i][2] -= 1
            
            if amount_amount == 0: break #EXIT

            if i_ready == None: #IDLE
                RET.append('idle')
                continue
            else: #RUN
                priority[i_ready][1] -= 1
                priority[i_ready][2] += n
                RET.append(priority[i_ready][0])
            
            priority = sorted(priority, key=(lambda x:x[1]), reverse = True) #SORT by current amounts
        return len(RET)

    def get_task_priority(self, tasks):
        tmp_dict = {}
        for task in tasks: #GET AMOUNT
            if tmp_dict.get(task):
                tmp_dict[task] += 1
            else:
                tmp_dict[task] = 1

        tmp_dict = sorted(tmp_dict.items(), key=(lambda x:x[1]), reverse = True) #SORT by amounts

        RET = [] #GET RET
        for d in tmp_dict:
            #name/amount/leaving_cooldown
            RET.append([d[0], d[1], 0])
        return RET

tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
s = Solution()
s.leastInterval(tasks, n)