import sh

def main():
    for results in zip(sh.python(m='parser_versions.v1_0.thinq_parser', 
                                 _env={'PYTHONPATH': 'parser_versions/v1_0'}, _iter=True, 
                                 _in=(f'test{i}\n' for i in range(10))),
                       sh.python(m='parser_versions.v1_1.thinq_parser', 
                                 _env={'PYTHONPATH': 'parser_versions/v1_1'}, _iter=True, 
                                 _in=(f'test{i}\n' for i in range(10)))):
        print(results)
    
if __name__ == "__main__":
    main()