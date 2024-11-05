from repository.repository import ADNRepository

class MutantService:
    def __init__(self):
        self.repository = ADNRepository()

    def is_mutant(self, dna):
        sequence_count = 0
        n = len(dna)

       
        for i in range(n):
            for j in range(n - 3):
                if dna[i][j] == dna[i][j+1] == dna[i][j+2] == dna[i][j+3]:
                    sequence_count += 1
                if dna[j][i] == dna[j+1][i] == dna[j+2][i] == dna[j+3][i]:
                    sequence_count += 1

       
        for i in range(n - 3):
            for j in range(n - 3):
                if dna[i][j] == dna[i+1][j+1] == dna[i+2][j+2] == dna[i+3][j+3]:
                    sequence_count += 1
                if dna[i+3][j] == dna[i+2][j+1] == dna[i+1][j+2] == dna[i][j+3]:
                    sequence_count += 1

        is_mutant = sequence_count > 1
        
        self.repository.save_dna(dna, is_mutant)
        return is_mutant

    def get_stats(self):
        count_mutant_dna = self.repository.count_mutant()
        count_human_dna = self.repository.count_human()
        ratio = count_mutant_dna / count_human_dna if count_human_dna > 0 else 0
        return {
            "count_mutant_dna": count_mutant_dna,
            "count_human_dna": count_human_dna,
            "ratio": ratio
        }