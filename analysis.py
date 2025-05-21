def analyze(dataset):
    # Procesamiento básico de datos
    return [x*2 for x in dataset if isinstance(x, int)]

if __name__ == "__main__":
    sample = [1, 2, 3, 4]
    print(analyze(sample))
