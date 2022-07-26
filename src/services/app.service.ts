import { Injectable } from '@nestjs/common';
import { documentClient } from 'src/config/dynamodb.config';
import { ChartRequest } from 'src/dto/chart.request';
import { generateHash } from './utils';

@Injectable()
export class AppService {
  getHello(): string {
    return 'Hello World!';
  }

  async getChart(request: ChartRequest) {
    var params = {
      TableName: 'reports_cache',
      Key: {
        ID: generateHash(request),
      }
    };

    documentClient.get(params, function (err, data) {
      if (err)
        console.log(err);
      else
        console.log(data);
      return data.Item;
    });

    return null;
  }

  async insertChart(request: ChartRequest) {
    documentClient
      .put({
        Item: {
          ID: generateHash(request),
          data: "sample chart",
        },
        TableName: "reports_cache",
      })
      .promise()
      .then(data => console.log(data.Attributes))
      .catch(console.error)

  }

}
