# Behaviour ROS

No codigo atual do behaviour foi inserido um subscriber que recebe as mensagens da visao do codigo finder.py. Para inicializar a comunicacao
com os demais nodes, foi criado um novo codigo, que possui a nomenclatura nome_modificado.py, baseado inteiramente nos codigos anteriores 
(brain.py, basic_goal.py e think.py) a fim de inicializar a ligacao com os demais nodes, inclusive o movimento. A ideia principal é configurar 
o brain para substituir o atual codigo "StateTransition.cpp e Stategy.cpp" para conversar diretamente com o codigo "movement.cpp".
