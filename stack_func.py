import copy
#スタックの初期化
def stack_new(def_values):
    if type(def_values)!=list:
        return[def_values]
    return copy.copy(def_values)

#スタックに値を追加
def stack_push(stack,v):
    stack.append(v)
    
#スタックから値をと出す
def stack_pop(stack):
    if len(stack)==0:
        return None
    value=stack[len(stack)-1]
    del stack[len(stack)-1]
    return value
#スタックをテストする関数
def test_stack():
    #
    st=stack_new([0,1])
    #
    stack_push(st,2)
    stack_push(st,3)
    #
    assert stack_pop(st)==3
    assert stack_pop(st)==2
    assert stack_pop(st)==1
    assert stack_pop(st)==0
    #
    st2=stack_new(1)
    stack_push(st2,2)
    assert stack_pop(st2)==2
    assert stack_pop(st2)==1
    assert stack_pop(st2) is None