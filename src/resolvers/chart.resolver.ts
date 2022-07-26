import { Resolver, Query, Args, ID } from '@nestjs/graphql';
import { Field, Int, ObjectType } from '@nestjs/graphql';
import { GetItemOutput } from 'aws-sdk/clients/dynamodb';
import { documentClient } from 'src/config/dynamodb.config';


@ObjectType()
class Chart {
  @Field(() => ID)
  ID!: string;

  @Field()
  data!: string;
}


@Resolver()
class ChartResolver {

  @Query(() => Chart)
  async getChart(@Args('id', { type: () => String }) id: string) {
    const result = await documentClient
      .get({
        TableName: "reports_cache",
        Key: {
          ID: id,
        },
      })
      .promise()
      .then(data => data.Item);

    console.log(result);
    return result;
  }

}

export { ChartResolver };