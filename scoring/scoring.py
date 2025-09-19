class AllScores:
    def __init__(self):
        self.scores = []
    
    def sort(self):
        scrs = self.scores
        for i in range(len(scrs)):
            curr = scrs[i]
            j = i-1
            while j >= 0 and scrs[j].score < curr.score:
                scrs[j+1] = scrs[j]
                j -= 1
            
            scrs[j+1] = curr
        
        self.scores = scrs

    def get_high_score(self):
        if self.scores:
            return self.scores[0].score
        else:
            return 0
    
    def insert_score(self, score):
        self.scores.append(score)
        while len(self.scores) > 100:
            self.scores.pop()
        self.sort()
        self.save_scores_to_file()
    
    def reset_scores(self):
        self.scores = []
        self.save_scores_to_file()
        self.get_scores_from_file()
    
    def get_scores_from_file(self):
        try:
            with open("./scoring/leaderboard.log") as f:
                file_contents = f.read()
            f.close()

            scores_list = file_contents.split('\n')
            for line in scores_list:
                line_list = line.split(' ')
                score = UserScore(int(line_list[0]), line_list[2])
                self.scores.append(score)
        
        except Exception as e:
            return f"{e}"

    def save_scores_to_file(self):
        try:
            with open("./scoring/leaderboard.log", "w") as f:
                scores = ""
                for score in self.scores:
                    scores += f"{score.score} - {score.diff}\n"
                f.write(scores)
            f.close()
        
        except Exception as e:
            return f"{e}"

class UserScore:
    def __init__(self, score, diff):
        self.score = score
        self.diff = diff
