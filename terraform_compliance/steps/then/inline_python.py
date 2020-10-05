import importlib.util
from radish import world

# later do something that remembers previous imports so that you don't re-import everything over and over again
def inline_python(_step_obj, file_name, function_name):

    if file_name in inline_python.file_names:
        mod = inline_python.file_names[file_name]

    else:
        path = _step_obj.path
        path = path[0:path.rfind('/')+1] + file_name

        spec = importlib.util.spec_from_file_location('user_imported', path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)

        inline_python.file_names[file_name] = mod

    f = getattr(mod, function_name)

    return f(_step_obj)

inline_python.file_names = {}


'''
Next up

Write a few When & Then steps with this
Figure out error functions (error, skip) & calling conventions
- should I create friendlier versions for them? Or should I let them figure their shit out

General Design
- Do they make a class and I import it?
- Do I make a user_test class?
- Do I make a decorator and let them use it? (Generates the necessary variables)

Kinda don't want to expose everything but don't want to limit functionality either

One Idea
- pass stash/resources
- error/skip that skips without the stepobj

right now just pass stash/_step_obj but you probably want to make a class or even make a class stub that other testers can import

'''