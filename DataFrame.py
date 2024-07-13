import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline


def preprocess_dataframe(df):
    """
    Cleans and preprocesses the given DataFrame by handling missing values,
    normalizing numerical columns, and encoding categorical columns.

    :param df: pandas DataFrame to be cleaned and preprocessed.
    :return: A cleaned and preprocessed DataFrame.
    """

    # Separate features into numerical and categorical columns
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns

    # Define a pipeline for numerical features
    numerical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])

    # Define a pipeline for categorical features
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    # Combine both pipelines into a single column transformer
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_cols),
            ('cat', categorical_transformer, categorical_cols)
        ]
    )

    # Fit and transform the data
    df_cleaned = preprocessor.fit_transform(df)

    # Get the feature names after transformation
    num_features = preprocessor.transformers_[0][2]
    cat_features = preprocessor.transformers_[1][1]['onehot'].get_feature_names_out(categorical_cols)

    # Combine numerical and encoded categorical feature names
    feature_names = list(num_features) + list(cat_features)

    # Convert the transformed array back to a DataFrame
    df_cleaned = pd.DataFrame(df_cleaned, columns=feature_names)

    return df_cleaned


# Example usage
if __name__ == "__main__":
    # Sample data
    data = {
        'age': [25, 30, np.nan, 35],
        'salary': [50000, 60000, 70000, np.nan],
        'gender': ['male', 'female', 'female', 'male'],
        'city': ['New York', np.nan, 'Los Angeles', 'Chicago']
    }
    df = pd.DataFrame(data)

    # Preprocess the DataFrame
    df_cleaned = preprocess_dataframe(df)

    print(df_cleaned)
