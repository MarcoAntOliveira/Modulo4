from pathlib import Path
from pyPDF2  import PdfReader # type:ignore

PASTA_RAIZ =  Path(__file__).parent

PASTA_ORIGINAIS = PASTA_RAIZ /'origin'
PASTA_NOVA = PASTA_RAIZ / 'edited'

RELATORIO_BACEN = PASTA_RAIZ/'R20230210.pdf'

PASTA_NOVA.mkdir(exist_ok= True)