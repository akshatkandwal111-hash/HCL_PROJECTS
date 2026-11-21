
import pandas as pd

print("========================================")
print(" E-COMMERCE & CONSUMER BEHAVIOUR ANALYSIS")
print("========================================")

# Reading CSV File

df = pd.read_csv("ecommerce_consumer_behaviour_30_customers.csv")


# Display Customer Data

print("\n========== CUSTOMER DATA ==========")
print(df.to_string(index=False))


# Total Customers

print("\nTotal Customers:", len(df))


# Sales Analysis

print("\n========== SALES ANALYSIS ==========")

print("Total Sales:", df["Amount"].sum())

print("Average Spending:", df["Amount"].mean())

print("Maximum Spending:", df["Amount"].max())

print("Minimum Spending:", df["Amount"].min())


# Highest Spending Customer

print("\n========== TOP CUSTOMER ==========")

highest = df.loc[df["Amount"].idxmax()]

print(highest)


# Category Analysis

print("\n========== CATEGORY ANALYSIS ==========")

print(df["Category"].value_counts())


# Payment Analysis

print("\n========== PAYMENT ANALYSIS ==========")

print(df["Payment"].value_counts())


# Shopping Frequency

print("\n========== SHOPPING FREQUENCY ==========")

print(df["Frequency"].value_counts())


# Gender Analysis

print("\n========== GENDER ANALYSIS ==========")

print(df["Gender"].value_counts())


# City Analysis

print("\n========== CITY ANALYSIS ==========")

print(df["City"].value_counts())


# Category-wise Revenue

print("\n========== CATEGORY-WISE REVENUE ==========")

print(df.groupby("Category")["Amount"].sum())


# Customer Satisfaction

print("\n========== CUSTOMER SATISFACTION ==========")

print("Average Rating:", df["Rating"].mean())

print("Highest Rating:", df["Rating"].max())

print("Lowest Rating:", df["Rating"].min())


# Final Conclusion

print("\n========== FINAL CONCLUSION ==========")

print("Most Popular Category:",
      df["Category"].mode()[0])

print("Most Popular Payment Method:",
      df["Payment"].mode()[0])

print("Most Common Shopping Frequency:",
      df["Frequency"].mode()[0])

print("\nAnalysis Completed Successfully!")
