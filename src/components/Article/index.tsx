import React from 'react';
import styles from './article.module.css';

interface ArticleProviderProps {
    children: React.ReactNode;
    start?: number;
}

export function ArticleProvider({ children, start = 0 }: ArticleProviderProps) {
    return (
        <div
            className={styles.provider}
            style={{ '--article-start': start } as React.CSSProperties}
        >
            {children}
        </div>
    );
}

export function Article() {
    return <h4 className={styles.header} />;
}

export function ArticleBis() {
    return <h4 className={styles.headerBis} />;
}
export function ArticleTer() {
    return <h4 className={styles.headerTer} />;
}
export function ArticleQuater() {
    return <h4 className={styles.headerQuater} />;
}