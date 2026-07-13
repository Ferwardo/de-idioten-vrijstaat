interface Book {
    pages: Record<string, number>;
}

export const books: Record<string, Book> = {
    "civil": {
        "pages": {
            "common": 0,
            "nationality": 6,
            "pensions": 10,
            "precedent": 12
        }
    },
    "penal": {
        "pages": {
            "common": 0,
            "fuck": 27,
            "not-good": 32,
            "oepsie": 35,
            "prosecution": 38
        }
    },
}