def custom_preprocessing_hook(endpoints):
    filtered = []
    for path, path_regex, method, callback in endpoints:
        if "gql" not in path:
            filtered.append((path, path_regex, method, callback))
    return filtered
