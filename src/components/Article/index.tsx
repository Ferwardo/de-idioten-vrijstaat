import React from 'react';
import styles from './article.module.css';
import { books } from './books';

interface ArticleProviderProps {
    children: React.ReactNode;
    book: string;
    page: string;
}

interface ArticleProps {
    children?: React.ReactNode;
}

export function ArticleProvider({ children, book, page }: ArticleProviderProps) {
    const start = books[book]?.pages[page] ?? 0;
    return (
        <div
            className={styles.provider}
            style={{ '--article-start': start } as React.CSSProperties}
        >
            {children}
        </div>
    );
}

export function Article({ children }: ArticleProps) {
    return (
        <h4 className={styles.header}>
            {children && <span>{children}</span>}
        </h4>
    );
}

export function ArticleBis({ children }: ArticleProps) {
    return (
        <h4 className={styles.headerBis}>
            {children && <span>{children}</span>}
        </h4>
    );
}
export function ArticleTer({ children }: ArticleProps) {
    return (
        <h4 className={styles.headerTer}>
            {children && <span>{children}</span>}
        </h4>
    );
}
export function ArticleQuater({ children }: ArticleProps) {
    return (
        <h4 className={styles.headerQuater}>
            {children && <span>{children}</span>}
        </h4>
    );
}