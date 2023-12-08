from python.src.files import *

def compare_files (outputPath: str, expectedPath: str):
    output = open(outputPath, "r")
    expected = open(expectedPath, "r")

    assert output.read() == expected.read()
    
    output.close()
    expected.close()

def test_path_readlines_no_endline():
    inputPath = "inputs/files_test/test_path_readlines_no_endline_normal.txt"
    expectedLines = [
        "   hola   ",
        "",
        " este es un ejemplo normal",
        "   comun    y    corriente",
        "una prueba   ",
        "",
        "",
        "prueba",
        ""
    ]
    assert path_readlines_no_endline(inputPath) == expectedLines

def test_path_writelines_newline_empty(tmp_path):
    lines = []
    outputPath = tmp_path / "test_path_writelines_newline_empty.out"
    expectedPath = "expected/files_test/test_path_writelines_newline_empty.txt"

    path_writelines_newline(lines, outputPath)

    compare_files(outputPath, expectedPath)

def test_path_writelines_newline_normal(tmp_path):
    lines = [
        "",
        "hola mundo",
        "   una prueba   ",
        "hi",
        "",
        "last one and it is a bit longer  "
    ]
    outputPath = tmp_path / "test_path_writelines_newline_normal.out"
    expectedPath = "expected/files_test/test_path_writelines_newline_normal.txt"

    path_writelines_newline(lines, outputPath)

    compare_files(outputPath, expectedPath)
