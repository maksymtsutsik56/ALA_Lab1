import numpy as np

def read_off(filename):
    with open(filename) as f:
        header = f.readline().strip()

        if header == "OFF":
            counts = f.readline()
        elif header.startswith("OFF"):
            counts = header[3:]  #broken files
        else:
            raise ValueError("Not a valid OFF file")

        n_verts, n_faces, _ = map(int, counts.split())
        verts = [list(map(float, f.readline().split())) for _ in range(n_verts)]
        faces = [list(map(int, f.readline().split()[1:])) for _ in range(n_faces)]

    return np.array(verts), faces

def sample_points(vertices, faces, n=50000):
    triangles = vertices[np.array(faces)]  

    a, b, c = triangles[:, 0], triangles[:, 1], triangles[:, 2]
    areas = np.linalg.norm(np.cross(b - a, c - a), axis=1) / 2
    idx = np.random.choice(len(triangles), size=n, p=areas / areas.sum())
    a, b, c = a[idx], b[idx], c[idx]

    u = np.random.rand(n, 1)
    v = np.random.rand(n, 1)
    outside = (u + v) > 1          
    u[outside] = 1 - u[outside]    
    v[outside] = 1 - v[outside]

    return a + u * (b - a) + v * (c - a)