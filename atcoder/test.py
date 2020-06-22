	"map int input": {
		"prefix": "mpi",
		"body": [
			"map(int,input().split())"
		],
		"description": "map int"
	}

	"list map int": {
		"prefix": "lmpi",
		"body": [
			"list(map(int,input().split()))"
		],
		"description": "list map int"
    }
    
    "resolve": {
		"prefix": "res",
		"body": [
			"def resolve():"
		],
		"description": "resolve"
    }

    "int input": {
		"prefix": "ii",
		"body": [
			"int(input())"
		],
		"description": "int input"
    }

    "dfs": {
		"prefix": "dfs",
		"body": [
			"def dfs(A):"
            "# 数列の長さが N に達したら打ち切り"
            "if len(A) == N:"
                "# 処理"
                "return"
            "for v in range(M):"
                "A.append(v)"
                "dfs(A)"
                "A.pop()"
		],
		"description": "dfs"
    }