from db.db_connection import session
# Importa ADNRecord dentro del método para evitar dependencia circular
class ADNRepository:
    def save_dna(self, dna, is_mutant):
        from models.dna_model import ADNRecord
        dna_str = ''.join(dna)
        if not session.query(ADNRecord).filter_by(dna=dna_str).first():
            record = ADNRecord(dna=dna_str, is_mutant=is_mutant)
            session.add(record)
            session.commit()

    def count_mutant(self):
        from models.dna_model import ADNRecord
        return session.query(ADNRecord).filter_by(is_mutant=True).count()

    def count_human(self):
        from models.dna_model import ADNRecord
        return session.query(ADNRecord).filter_by(is_mutant=False).count()