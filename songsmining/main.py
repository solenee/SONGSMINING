import preprocess

PRINCIPAL_TRAINING_RAW="/comptes/E15D861C/Bureau/ProjetRI/Corpora/Beyonce/beyonce.training"
PRINCIPAL_TRAINING="/comptes/E15D861C/Bureau/ProjetRI/Corpora/Beyonce/beyonce.clean.training"
if __name__ == "__main__":
  preprocess.formatSequence(PRINCIPAL_TRAINING_RAW, PRINCIPAL_TRAINING)
