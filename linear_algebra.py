def add_vector_mag_dir(x=(), y=()):
    X = (x[0] * math.cos(math.radians(x[1]))) + (y[0] * math.cos(math.radians(y[1])))
    Y = (x[0] * math.sin(math.radians(x[1]))) + (y[0] * math.sin(math.radians(y[1])))
    return (X, Y)

 