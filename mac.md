 # <<< conda init <<<
export PATH="/anaconda3/bin:$PATH"
export SPARK_HOME="/usr/local/opt/spark"
export PYSPARK_DRIVER_PYTHON="jupyter"
export PYSPARK_DRIVER_PYTHON_OPTS="notebook"
export PYSPARK_PYTHON=python3
alias snotebook='$SPARK_HOME/bin/pyspark --master local[2]'