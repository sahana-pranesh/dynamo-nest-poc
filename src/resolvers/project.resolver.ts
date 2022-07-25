import { Resolver, Query, Args, ID } from '@nestjs/graphql';
import { Field, Int, ObjectType } from '@nestjs/graphql';
import { GetItemOutput } from 'aws-sdk/clients/dynamodb';
import { DocumentClient } from './config';


@ObjectType()
class Project {
  @Field(() => ID)
  ID!: string;

  @Field()
  data!: string;
}


@Resolver()
class ChartResolver {

  @Query(() => String)
  sayHello(): string {
    return 'Hello World!';
  }

  @Query(() => Project)
  async getChart(@Args('id', { type: () => String }) id: string) {
    const result = await DocumentClient
      .get({
        TableName: "projects_cache",
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