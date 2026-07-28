from client import SeoBacklinkAnalyzerClient

def main():
    client = SeoBacklinkAnalyzerClient()
    res = client.analyze_backlinks(domain='example.com')
    print(f"Result for opportunity_score: {res['opportunity_score']}")

if __name__ == "__main__":
    main()
