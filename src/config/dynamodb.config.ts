import { DynamoDB } from "aws-sdk";

export const DocumentClient = new DynamoDB.DocumentClient({
    sslEnabled: false,
    endpoint: `http://localhost:4566`,
    accessKeyId: 'mock',
    secretAccessKey: 'mock',
    region: 'ap-southeast-2',

  });